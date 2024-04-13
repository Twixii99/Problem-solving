function ListNode(val, next) {
  this.val = (val === undefined ? 0 : val)
  this.next = (next === undefined ? null : next)
}

export default function buildList(nums) {
  let list = new ListNode(-1, null);
  let ptr = list;
  for (let num of nums) {
    ptr.next = new ListNode(num);
    ptr = ptr.next;
  }
  return list.next;
}

export function printList(head) {
  let itr = head;
  let listValues = [];
  while (itr) {
    listValues.push(itr.val);
    itr = itr.next;
  }
  console.log(listValues);
}