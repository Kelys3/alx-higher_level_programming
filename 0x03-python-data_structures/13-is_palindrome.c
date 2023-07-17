#include "lists.h"


/**
  * is_palindrome - Checks if a singly linked list is a palindrome
  * @head: The head of the singly linked list
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int i = 0, len = 0, len_cyc = 0, len_list = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	start = *head;
	len = count_listint_len(start);
	len_cyc = len * 2;
	len_list = len_cyc - 2;
	end = *head;

	for (; i < len_cyc; i = i + 2)
	{
		if (start[i].n != end[len_list].n)
			return (0);
		len_list = len_list - 2;
	}
	return (1);
}

/**
  * get_node - Gets a node from a linked list
  * @head: The head of the linked list
  * @index: The index to find in the linked list
  *
  * Return: The specific node of the linked list
  */
listint_t *get_node(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int num = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (num == index)
				return (current);

			current = current->next;
			++num;
		}
	}

	return (NULL);
}

/**
  * count_listint_len - counts the number of elements in a linked list
  * @head: linked list to count
  *
  * Return: number of elements in the linked list
  */
size_t count_listint_len(const listint_t *head)
{
	int length = 0;

	while (head != NULL)
	{
		++length;
		head = head->next;
	}

	return (length);
}
