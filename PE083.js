const fs = require("fs");

let n = 80;

let grid = fs
  .readFileSync("p081_matrix.txt")
  .toString()
  .split("\n");
for (let row = 0; row < grid.length; ++row) {
  grid[row] = grid[row].split(",");
}
for (let row = 0; row < grid.length; ++row) {
  for (let col = 0; col < grid[row].length; ++col) {
    grid[row][col] = parseInt(grid[row][col]);
  }
}
grid.pop();
// console.log(grid[79], typeof grid[0][0], grid.length, grid[0].length);

const isPresent = v => {
  for (let i = 0; i < queue.length; ++i) {
    if (v === queue[i]) {
      return true;
    }
  }
  return false;
};
const createNode = (row, col, dist) => {
  return {
    row,
    col,
    id: row * n + col,
    dist
  };
};

let dist = [];
for (let row = 0; row < n; ++row) {
  for (let col = 0; col < n; ++col) {
    dist.push(createNode(row, col, Number.POSITIVE_INFINITY));
  }
}
dist[0].dist = grid[0][0];

let queue = [];
let prev = [];
for (let i = 0; i < n * n; ++i) {
  queue.push(i);
  prev.push(undefined);
}

const extractU = () => {
  let newDist = [];
  for (let index = 0; index < dist.length; ++index) {
    if (isPresent(dist[index].id)) {
      newDist.push(dist[index]);
    }
  }
  newDist.sort((a, b) => a.dist - b.dist);
  return newDist.shift();
};

while (queue.length > 0) {
  let u = extractU();
  console.log(u);
  queue.splice(queue.indexOf(u.id), 1);
  if (u.row - 1 >= 0) {
    //top
    if (
      dist[(u.row - 1) * n + u.col].dist >
      dist[u.row * n + u.col].dist + grid[u.row - 1][u.col]
    ) {
      dist[(u.row - 1) * n + u.col].dist =
        dist[u.row * n + u.col].dist + grid[u.row - 1][u.col];
      prev[(u.row - 1) * n + u.col] = u.row * n + u.col;
    }
  }
  if (u.col + 1 < 80) {
    //right
    if (
      dist[u.row * n + (u.col + 1)].dist >
      dist[u.row * n + u.col].dist + grid[u.row][u.col + 1]
    ) {
      dist[u.row * n + (u.col + 1)].dist =
        dist[u.row * n + u.col].dist + grid[u.row][u.col + 1];
      prev[u.row * n + (u.col + 1)] = u.row * n + u.col;
    }
  }
  if (u.row + 1 < 80) {
    //bottom
    if (
      dist[(u.row + 1) * n + u.col].dist >
      dist[u.row * n + u.col].dist + grid[u.row + 1][u.col]
    ) {
      dist[(u.row + 1) * n + u.col].dist =
        dist[u.row * n + u.col].dist + grid[u.row + 1][u.col];
      prev[(u.row + 1) * n + u.col] = u.row * n + u.col;
    }
  }
  if (u.col - 1 >= 0) {
    //left
    if (
      dist[u.row * n + (u.col - 1)].dist >
      dist[u.row * n + u.col].dist + grid[u.row][u.col - 1]
    ) {
      dist[u.row * n + (u.col - 1)].dist =
        dist[u.row * n + u.col].dist + grid[u.row][u.col - 1];
      prev[u.row * n + (u.col - 1)] = u.row * n + u.col;
    }
  }
}

console.log(dist[6399]);
console.log(prev);
