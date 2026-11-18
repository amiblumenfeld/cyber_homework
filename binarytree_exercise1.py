import binarytree


def count_values(root):
    counts = {}

    def visit(node):
        if node is None:
            return
        counts[node.value] = counts.get(node.value, 0) + 1
        visit(node.left)
        visit(node.right)

    visit(root)
    return counts

def value_to_lst(input_value):
    values = []
    for value in input_value.split(","):
        if value.strip().lower() == "none":
            values.append(None)
        
        elif value.strip().isnumeric():
            values.append(int(value.strip()))
        else:
            values.append(str(value.strip()))
    return values

def list_to_dict(lst):
    counts = {}
    for value in lst:
        if value is not None:
            counts[value] = counts.get(value, 0) + 1
    return counts


def main():
    try:
        """root1 = binarytree.tree()
        print(root1)
        print(count_values(root1))"""
        values1 = [1, 1, 3, "a", 5, 6, 6, None, 3,"f!"]
        root2 = binarytree.build(values1)
        print(root2)
        dic1 = count_values(root2)
        print(dic1)

        input_value=input("Enter a list of values separated by commas (for example: 1,2,3,a,*,None): ")
        lst=value_to_lst(input_value)
        dic2=list_to_dict(lst)
        if dic1==dic2:
            print("The list is equal to the dictionary.")
        else:
            print("The list is not equal to the dictionary.")
    except RecursionError:
        print("Recursion Error")
        return
    except Exception:
        print("There is a bug")
        return

if __name__ == "__main__":
    main()