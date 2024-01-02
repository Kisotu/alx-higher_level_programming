#include "lists.h"

/**
 * insert_node - Fxn that inserts a number into a sorted singly-linked list.
 * @head: Points to the head of the linked list.
 * @number: The number to insert.
 * Return: A pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *start, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*start = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
