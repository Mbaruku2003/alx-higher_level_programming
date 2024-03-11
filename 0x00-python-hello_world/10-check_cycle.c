#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <strings.h>
/**
 * check_cycle - checks for a circular list
 * @list: the list being checked
 */
int check_cycle(listint_t *list)
{
	listint_t *oncemove;
	listint_t *twicemove;

	if (list == NULL || list->next == NULL)
		return (0);
	oncemove = list;
	twicemove = list;
	while (oncemove != NULL && twicemove != NULL && twicemove->next != NULL)
	{
		oncemove = oncemove->next;
		twicemove = twicemove->next->next;

		if (oncemove == twicemove)
		{
			return (1);
		}
	}
	return (-1);
}
