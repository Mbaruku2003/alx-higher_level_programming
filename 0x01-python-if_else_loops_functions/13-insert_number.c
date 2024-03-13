#include <stdio.h>
#include <unistd.h>
#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a node
 * @head: list of heads
 * @number: the number of nodes address
 * Return: pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *temporary = NULL;
	listint_t *current = *head;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if(*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < number)
		{
			temporary = current;
			current = current->next;
		}
		temporary->next = new;
		new->next = current;
	}
	return (new);
}
