// getCmdRet.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//
#include <iostream>
#include <Windows.h>

bool getCmdRet(const std::wstring& cmd, std::string& retstr)
{
	SECURITY_ATTRIBUTES sa;
	HANDLE hRead, hWrite;

	sa.nLength = sizeof(SECURITY_ATTRIBUTES);
	sa.lpSecurityDescriptor = NULL;
	sa.bInheritHandle = TRUE;

	if (!CreatePipe(&hRead, &hWrite, &sa, 0))
	{
		return FALSE;
	}

	WCHAR command[1024];
	//wcscpy_s(command, L"cmd.exe /C");
	//wcscat_s(command, cmd.c_str());

	wcscpy_s(command, cmd.c_str());

	STARTUPINFO si;
	PROCESS_INFORMATION pi;
	si.cb = sizeof(STARTUPINFO);

	GetStartupInfo(&si);

	si.hStdError = hWrite;            //把创建进程的标准错误输出重定向到管道输入
	si.hStdOutput = hWrite;           //把创建进程的标准输出重定向到管道输入
	si.wShowWindow = SW_HIDE;
	si.dwFlags = STARTF_USESHOWWINDOW | STARTF_USESTDHANDLES;

	if (!CreateProcess(NULL, command, NULL, NULL, TRUE, NULL, NULL, NULL, &si, &pi))
	{
		CloseHandle(hWrite);
		CloseHandle(hRead);
		CloseHandle(pi.hProcess);
		CloseHandle(pi.hThread);
		return FALSE;
	}
	CloseHandle(hWrite);

	char buffer[4096] = { 0 }; //用4K的空间来存储输出的内容，只要不是显示文件内容，一般情况下是够用了。
	DWORD bytesRead;
	while (true)
	{
		if (ReadFile(hRead, buffer, 4095, &bytesRead, NULL) == NULL)
			break;
		
		retstr.append(buffer);		
		memset(buffer, 0, sizeof buffer);
	}

	CloseHandle(hRead);

	CloseHandle(pi.hProcess);
	CloseHandle(pi.hThread);

	return TRUE;
}

int main()
{
	std::wstring cmd = L"powershell.exe \"Get-Hotfix | select HotFixID\"";
	std::string retstr;
	getCmdRet(cmd, retstr);
	std::cout << "************\n" << retstr.c_str() << "************\n" << std::endl;

	if (std::string::npos != retstr.find("KB4580980"))
	{
		std::cout << "find" << std::endl;
	}
	else
	{
		std::cout << "not find" << std::endl;
	}
	getchar();
	return 0;
}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
