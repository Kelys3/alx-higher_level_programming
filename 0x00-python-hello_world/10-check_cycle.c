#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *forward, *fast_forward;

	forward = list;
	fast_forward = list;

	while (fast_forward && fast_forward->next)
	{
		forward = forward->next;
		fast_forward = fast_forward->next->next;

		if (fast_forward == forward)
		{
			return (1);
		}
	}
	return (0);
}
