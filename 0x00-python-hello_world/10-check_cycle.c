#include "lists.h"

/**
 * check_cycle - fxn that checks if a linked list contains a cycle
 * @list: the list to check
 * Return: 1 if cycle exists, 0 if it doesn't
 */
int check_cycle(listint_t *last)
{
	listint_t *once = list;
	listint_t *twice = list;

	if (!list)
		return (0);

	while (once && twice && twice->next)
	{
		once = once->next;
		twice = twice->next->next;
		if (once == twice)
			return (1);
	}
	return (0);
}
