#include <stdio.h>
#include<stdbool.h>
#include<stdlib.h>
 
struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
};

void push(struct Node** head_ref, int new_c)
{
    struct Node* new_node =
            (struct Node*) malloc(sizeof(struct Node));
    new_node->data = new_c;
    new_node->prev = NULL;
    new_node->next = (*head_ref);
    if ((*head_ref) != NULL)
        (*head_ref)->prev = new_node;
     *head_ref = new_node;
}

bool isCircular(struct Node *head){
 struct Node *temp=head;
 while(temp!=NULL)
 { //if temp points to head then it has completed a circle,thus a circular linked list.
    if(temp->next==head)
        return true;
    temp=temp->next;
}

return false;

}
int main(void)
{
    struct Node* head = NULL;
    push(&head, 5);
    push(&head, 4);
    push(&head, 3);
    push(&head, 2);
    push(&head, 1);
    
    if(isCircular(head))
        printf("Yes\n");
    else
        printf("No\n");
 
}


// </stdlib.h></stdbool.h></stdio.h>