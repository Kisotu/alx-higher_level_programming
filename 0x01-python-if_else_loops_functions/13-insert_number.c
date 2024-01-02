#include "lists.h"

/**
 * insert_node - Fxn that inserts a number into a sorted singly-linked list.
 * @head: Points to the head of the linked list.
 * @number: The number to insert.
 * Return: A pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list_node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (list_node == NULL || list_node->n >= number)
	{
		new->next = list_node;
		*head = new;
		return (new);
	}

	while (list_node && list_node->next && list_node->next->n < number)
		list_node = list_node->next;

	new->next = list_node->next;
	list_node->next = new;

	return (new);
}
