#include "lists.h"

/**
 * check_cycle - fxn that checks if a linked list contains a cycle
 * @list: the list to check
 * Return: 1 if cycle exists, 0 if it doesn't
 */
int check_cycle(listint_t *last)
{
	listint_t *curr, *prev;

	if(!list)
	{
		return (0);
	}
	curr = list;
	prev = list->next;

	while (prev && curr && prev->next)
	{
		if (curr == prev)
		{
			return (1);
		}
		curr = curr->next;
		prev = prev->next->next;
	}
	return (0);
}
