#include "lists.h"
/**
 * check_cycle - checks if linked list iterates
 * list: list to be checked
 *
 * Return: 0 or 1 if it iterates
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (current != NULL)
	{
		if (current->n == -1)
		{
			return 1;
		}


		current->n = -1;

		current = current->next;
	}

	return 0;
}
