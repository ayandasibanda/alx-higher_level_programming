#include "lists.h"

/**
 * print_dlistint - Prints all the elements of a dlistint_t list.
 * @h: Pointer to the head of the linked list.
 * Return: The number of nodes in the list.
 */
size_t print_dlistint(const dlistint_t *h)
{
    size_t node_count = 0; /* Initialize the node count */

    /* Traverse the linked list */
    while (h != NULL)
    {
        printf("%d\n", h->n); /* Print the current node's value */
        h = h->next; /* Move to the next node */
        node_count++; /* Increment the node count */
    }

    return node_count; /* Return the total number of nodes */
}

