#include "lists.h"
/**
 * check_cycle - check if a list contains a loop
 * @list: head of list
 *
 * Return: 1 if looṕ exists, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *checker;

	if (list == NULL)
		return (0);

	current = list;
	checker = list;

	while (checker != NULL && checker->next != NULL)
	{
		current = current->next;
		checker = checker->next->next;

		if (current == checker)
			return (1);
	}
	return (0);
}
