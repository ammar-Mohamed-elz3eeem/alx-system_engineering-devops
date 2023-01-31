#include <stdio.h>
#include <unistd.h>
#include <wait.h>

/**
 * infinite_while - function to run after creating all processess
 * Return: 0 on killing
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point for zombie proccess
 * Return: 0 on success, 1 otherwise
 */

int main(void)
{
	int i = 0;
	pid_t zombie_pid;

	while (i < 5)
	{
		zombie_pid = fork();
		if (!zombie_pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)zombie_pid);
		i++;
	}
	if (zombie_pid != 0)
		infinite_while();
	return (0);
}
