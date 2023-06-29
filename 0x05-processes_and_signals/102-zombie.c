#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop
 *
 * Return: Always 0
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
 * main - Entry point of the program
 *
 * Return: Always 0
 */
int main(void)
{
	pid_t cZombie;
	int i;

	for (i = 0; i < 5; i++)
	{
		cZombie = fork();

		if (cZombie == 0)
		{
			exit(0);
		}
		else if (cZombie > 0)
		{
			printf("Zombie process created, PID: %d\n", cZombie);
			sleep(1);
		}
		else
		{
			fprintf(stderr, "Fork failed\n");
			return (1);
		}
	}

	infinite_while();

	return (0);
}
