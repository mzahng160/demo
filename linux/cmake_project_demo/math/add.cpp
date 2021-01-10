#include <iostream>
#include "add.h"

int add(int t1, int t2)
{
	int result = t1 + t2;

    std::cout << t1 << " + " << t2 << " is: " << result << std::endl;

    return result;
}