public class MultiStack {
  private StackInfo[] info;
  private int[] values;

  private class StackInfo {
    public int start, capacity, size;

    public StackInfo(int start, int capacity) {
      this.start = start;
      this.capacity = capacity;
    }

    public boolean isWithinStackCapacity(int index) {
      if (index <= 0 || index >= values.length)
        return false;
      int contigousIndex = index < start ? index + values.length : index;
      int end = start + capacity;

      return start <= contigousIndex && contigousIndex < end;
    }

    public int lastCapacityIndex() {
      return adjustIndex(start + capacity - 1);
    }

    public int lastElementIndex() {
      return adjustIndex(start + size - 1);
    }

    public boolean isFull() {
      return size == capacity;
    }

    public boolean isEmpty() {
      return size == 0;
    }
  }

  public MultiStack(int noOfStacks, int defaultSize) {
    info = new StackInfo[noOfStacks];
    for(int i = 0; i < noOfStacks; i++) {
      info[i] = new StackInfo(defaultSize * i, defaultSize);
    }
    values = new int[noOfStacks * defaultSize];
  }

  public void push(int stackNum, int value) {
    if(allStacksAreFull()) {
      System.out.println("All stacks are full");
      return;
    }
    StackInfo stackInfo = info[stackNum];
    if(stackInfo.isFull()) {
      expand(stackNum);
    }
    stackInfo.size++;
    values[stackInfo.lastElementIndex()] = value;
  }

  public int pop(int stackNum) {
    StackInfo stackInfo = info[stackNum];
    if(stackInfo.isEmpty()) {
      System.out.println("Stack is empty");
      return 0;
    }
    int value = values[stackInfo.lastElementIndex()];
    values[stackInfo.lastElementIndex()] = 0;
    stackInfo.size--;
    return value;
  }

  private void shift(int stackNum) {
    System.out.println("Shifting stack " + stackNum);
    StackInfo stackInfo = info[stackNum];
    if(stackInfo.size >= stackInfo.capacity) {
      int nextStack = (stackNum + 1) % info.length;
      shift(nextStack);
      stackInfo.capacity++;
    }

    int index = stackInfo.lastElementIndex();
    while(stackInfo.isWithinStackCapacity(index)) {
      values[index] = values[previousIndex(index)];
      index = previousIndex(index);
    }

    values[stackInfo.start] = 0;
    stackInfo.start = nextIndex(stackInfo.start);
  }

  private void expand(int stackNum) {
    shift((stackNum + 1) % info.length);
    info[stackNum].capacity++;
  }

  public int numberOfElements() {
    int size = 0;
    for(StackInfo sd: info) {
      size += sd.size;
    }

    return size;
  }

  public boolean allStacksAreFull() {
    return values.length == numberOfElements();
  }

  private int adjustIndex(int index) {
    int max = values.length;
    return ((index % max) + max) % max;
  }

  private int previousIndex(int index) {
    return this.adjustIndex(index - 1);
  }

  private int nextIndex(int index) {
    return this.adjustIndex(index + 1);
  }

}
