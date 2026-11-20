import binarytree

def characters(root):
    char_tree = []

    def visit(node):
        if node is None:
            return
        visit(node.left)
        char_tree.append(node.value)
        visit(node.right)
        

    visit(root)
    return char_tree

def palindrome(char_tree):
    reverse_tree = char_tree[::-1]
    if char_tree == reverse_tree:
        return True
    else:
        return False
def main():
    try:

        values1 = ['a','b','b','c','g', 'g','c','d','e',None, None, None, None,'e', 'd']
        values2 = ['a','b','b','c','g', 'g','c','d','e',None, None, None, None,'e', 'f']
        root1 = binarytree.build(values1)
        root2 = binarytree.build(values2)
        print(root1)
        char_tree1 = characters(root1)
        print(palindrome(char_tree1))

        print(root2)
        char_tree2 = characters(root2)
        print(palindrome(char_tree2))
        
    except RecursionError:
        print("Recursion Error")
        return
    except Exception:
        print("There is a bug")
        return

if __name__ == "__main__":
    main()