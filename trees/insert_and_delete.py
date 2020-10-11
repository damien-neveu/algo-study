from trees.node import Node


def insert_node(node, val):
    if node.data == val:
        return
    elif val < node.data:
        if node.left is None:
            node.left = Node(val)
        elif node.left.data < val: # insert in between
            node.left = Node(val, Node(node.left.data, node.left, None))
        else:
            insert_node(node.left, val)
    else: # val > root
        if node.right is None:
            node.right = Node(val)
        elif node.right.data > val: # insert in-between
            node.right = Node(val, None, node.right)
        else:
            insert_node(node.right, val)
    return node

# js solution
# function insertNode(node, val) {
# 	if (!node) {
#     return null;
#   }
#   let parent = node, curr = node;
#   while (curr) {
#     parent = curr;
#     if (curr.val === val) {
#       return null;
#     }
#     curr = curr.val > val ? curr.left : curr.right;
#   }
#   if (parent.val > val) {
#     parent.left = { val, left: null, right: null };
#   } else if (parent.val < val) {
#     parent.right = { val, left: null, right: null };
#   }
#   return node;
# }

def delete_node(node, val):
    if node is None:
        return
    if node.data > val:
        if node.left and node.left.data == val:
            node.left = Node(node.left.left.val, node.left)
        delete_node(node.left, val)
    elif node.data < val:
        delete_node(node.right, val)
    else:
        return

# js solution
# https://codeshare.io/2WYxQd
# function deleteNode(node, val)
# {
# if (!node)
# {
# return null;
# }
# if (val < node.val) {
# node.left = deleteNode(node.left, val);
# } else if (val > node.val) {
# node.right = deleteNode(node.right, val);
# } else {
# if (!node.left) {
# return node.right
# } else if (!node.right) {
# return node.left;
# }
# let
# minNode = node.right;
# while (minNode & & minNode.left) {
# minNode = minNode.left;
# }
# node.val = minNode.val;
# node.right = deleteNode(node.right, minNode.val);
# }
# return node;
# }

