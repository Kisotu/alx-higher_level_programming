#include "lists.h"

/**
 * reverse_listint - func to reverse a linked list
 * @head: pointer to first node of list
 * Return: pojnter to first node
 */
void reverse_listint(listint_t **head)
{
        listint_t *curr = *head;
        listint_t *prev = NULL;
        listint_t *next = NULL;

        while (curr)
        {
                next = curr->next;
                curr->next = prev;
                prev = curr;
                curr = next;
        }

        *head = prev;
}

/**
 * is_palindrome - func to check if a list is a palindrome
 * @head: pointer to first node
 * Return: 1 if palindroe, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *once = *head, *twice = *head, *tempo = *head, *dupl = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		twice = twice->next->next;
		if (!twice)
		{
			dupl = once->next;
			break;
		}
		if (!twice->next)
		{
			dupl = once->next->next;
			break;
		}
		once = once->next;
	}

	reverse_listint(&dupl);

	while (dupl && tempo)
	{
		if (tempo->n == dupl->n)
		{
			dupl = dupl->next;
			tempo = tempo->next;
		}
		else
			return (0);
	}
	if (!dupl)
		return (1);

	return (0);
}
