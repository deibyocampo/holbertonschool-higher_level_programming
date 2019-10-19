#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of a linked list
 * Return: 1 if polindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int arr[10240];
	int i, j;
	int len;

	ptr = *head;

	while (ptr != NULL)
	{
		ptr = ptr->next;
		len++;
	}

	ptr = *head;

	i = 0;
	while (ptr != NULL)
	{
		arr[i] = ptr->n;
		ptr = ptr->next;
		i++;
	}

	i--;
	j = 0;

	while (j <= len / 2)
	{
		if (arr[j] != arr[i])
			return (0);
		i--;
		j++;
	}
	return (1);
}
