#include "lists.h"
/**
 * *insert_node - in the linked list insert nwe node
 * @head: double pointer
 * @number: date into new node
 * Return: new node in the list or null if list is failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *tmp;

	tmp = *head;

	node = malloc(sizeof(listint_t));

	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;

	if (*head == NULL)
	{
		*head = node;
		return (node);
	}

	while (tmp->next != NULL)
	{
		if (tmp->next->n >= number)
		{
			node->next = tmp->next;
			tmp->next = node;
			return (node);
		}
		tmp = tmp->next;
	}
	return (node);
}
