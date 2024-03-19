#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
void reverse(listint_t **head);
int comparer(listint_t *head, listint_t *middle, int len);
/**
 * is_palindrome -checks if a singly linked list is a palinsdrome
 * @head: pointer to first node
 * Return: 0 if a palindrome is detected and 1 if yes
 */
int is_palindrome(listint_t **head)
{
	int len;
	int i;
	listint_t *temp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	middle = *head;
	for (len = 0; temp != NULL; len++)
		temp = temp->next;
	len = len / 2;
	for (i = 1; i < len; i++)
		middle = middle->next;
	if (len % 2 != 0 && len != 1)
	{
		middle = middle->next;
		len = len - 1;
	}
	reverse(&middle);
	i = comparer(*head, middle, len);
	return (i);
}
/**
 * comparer - compares two lists
 * @head: pointer to the head
 * middle: pointer to the middle
 * len: length of the list
 * Return : 1 if same else 0
 */
int comparer(listint_t *head, listint_t *middle, int len)
{
	int i;

	if (head == NULL || middle == NULL)
		return (1);
	for (i = 0; i < len; i++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);
}
/**
 * reverse- reverses a list
 * @head: pointer o the head to reverse
 */
void reverse(listint_t **head)
{

	listint_t *current;
	listint_t *next;
	listint_t *prev;

	if (head == NULL || *head == NULL)
		return;
	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current ->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
