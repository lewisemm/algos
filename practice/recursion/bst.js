function BinarySearchNode(value) {
  this.value = value;
  this.left = null;
  this.right = null
}

BinarySearchNode.prototype.add = function(value) {
  if (this.value <= value) {
    if (this.right === null) {
      this.right = new BinarySearchNode(value)
    }
    else {
      this.right.add(value)
    }
  }
  if (this.value > value) {
    if (this.left === null) {
      this.left = new BinarySearchNode(value)
    }
    else {
      this.left.add(value)
    }
  }
}

let bst = new BinarySearchNode(8)
console.log(bst)
console.log('Adding 3 and 10...\n')
bst.add(3)
bst.add(10)
console.log(bst)
console.log('Adding 1, 6, 11 and 14...\n')
bst.add(1)
bst.add(6)
bst.add(11)
bst.add(14)
console.log(bst)
console.log('Adding 9...\n')
bst.add(9)
console.log(bst)