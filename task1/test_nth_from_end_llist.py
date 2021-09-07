from nth_from_end_llist import LinkedList
import traceback


llist1 = LinkedList()
llist2 = LinkedList()
llist3 = LinkedList()
llist4 = LinkedList()
llist5 = LinkedList()

# llist1
lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
for i in lst1:
  llist1.push(i)

# llist2
lst2 = ["a", "b", "c", "d", "e", "f", "g", "h"]
for i in lst2:
  llist2.push(i)

# llist3
lst3 = [1, "first", 3, "second", 5, 6, "third", 8]
for i in lst3:
  llist3.push(i)

# llist4
lst4 = [1, 26, 3, 45, 65, 6, 71, 8]
for i in lst4:
  llist4.push(i)

# llist5
lst5 = [1, True, False, 4, True, True, 7, 8]
for i in lst5:
  llist5.push(i)


def test_nth_from_end_llist():
  assert llist1.nth_from_end(1) == 1
  assert llist1.nth_from_end(3) == 3
  assert llist1.nth_from_end(5) == 5

  assert llist2.nth_from_end(1) == "a"
  assert llist2.nth_from_end(3) == "c"
  assert llist2.nth_from_end(5) == "e"

  assert llist3.nth_from_end(2) == "first"
  assert llist3.nth_from_end(4) == "second"
  assert llist3.nth_from_end(6) == 6

  assert llist4.nth_from_end(2) == 26
  assert llist4.nth_from_end(4) == 45
  assert llist4.nth_from_end(7) == 71

  assert llist5.nth_from_end(1) == 1
  assert llist5.nth_from_end(3) == False
  assert llist5.nth_from_end(5) == True


if __name__ == "__main__":
  try:
    test_nth_from_end_llist()
    print("PASS")
  except:
    print("FAIL")
    traceback.print_exc()