#!include <stdio.h>
#include <stdlib.h>
#include "lists.h"
dlistint_t *add_dnodeint(dlistint_t **head, const int n);
{
	dlistint_t *h;
	dlistint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->prev = NULL;
	h = *head;
	if (h != NULL)
	{
		while (h->prev != NULL)
			h = h->prev;
	}
	new->next = h;
	if (h != NULL)
		h->prev = new;
}
