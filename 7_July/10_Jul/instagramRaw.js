const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Data storage
const users = [];
const posts = [];
const comments = [];

// Helper functions
function findUser(username) {
  return users.findIndex(user => user.username === username);
}

function findPost(postId) {
  return posts.findIndex(post => post.id === postId);
}

// Main functions
function registerUser(username) {
  if (findUser(username) === -1) {
    users.push({ username, following: [] });
    console.log(`User ${username} registered successfully.`);
  } else {
    console.log('Username already exists.');
  }
}

function followUser(currentUser, userToFollow) {
  const currentUserIndex = findUser(currentUser);
  const userToFollowIndex = findUser(userToFollow);

  if (currentUserIndex !== -1 && userToFollowIndex !== -1) {
    users[currentUserIndex].following.push(userToFollow);
    console.log(`${currentUser} is now following ${userToFollow}.`);
  } else {
    console.log('One or both users not found.');
  }
}

function createPost(username, content) {
  const postId = posts.length + 1;
  posts.push({ id: postId, username, content, likes: [] });
  console.log(`Post created with ID: ${postId}`);
}

function likePost(username, postId) {
  const postIndex = findPost(postId);
  if (postIndex !== -1) {
    const post = posts[postIndex];
    if (!post.likes.includes(username)) {
      post.likes.push(username);
      console.log(`${username} liked post ${postId}`);
    } else {
      console.log('You have already liked this post.');
    }
  } else {
    console.log('Post not found.');
  }
}

function commentOnPost(username, postId, content) {
  const postIndex = findPost(postId);
  if (postIndex !== -1) {
    comments.push({ postId, username, content });
    console.log('Comment added successfully.');
  } else {
    console.log('Post not found.');
  }
}

function displayPost(postId) {
  const postIndex = findPost(postId);
  if (postIndex !== -1) {
    const post = posts[postIndex];
    console.log(`Post ${post.id} by ${post.username}:`);
    console.log(post.content);
    console.log(`Likes: ${post.likes.length}`);
    console.log('Comments:');
    comments.filter(comment => comment.postId === postId).forEach(comment => {
      console.log(`${comment.username}: ${comment.content}`);
    });
  } else {
    console.log('Post not found.');
  }
}

function displayFeed(username) {
  const userIndex = findUser(username);
  if (userIndex !== -1) {
    const following = users[userIndex].following;
    const feed = posts.filter(post => following.includes(post.username) || post.username === username);
    feed.forEach(post => {
      console.log(`Post ${post.id} by ${post.username}:`);
      console.log(post.content);
      console.log(`Likes: ${post.likes.length}`);
      console.log('---');
    });
  } else {
    console.log('User not found.');
  }
}

// Main program loop
function mainLoop() {
  rl.question('Enter command (register, follow, post, like, comment, display, feed, exit): ', (command) => {
    switch (command.toLowerCase()) {
      case 'register':
        rl.question('Enter username: ', (username) => {
          registerUser(username);
          mainLoop();
        });
        break;
      case 'follow':
        rl.question('Enter your username: ', (currentUser) => {
          rl.question('Enter username to follow: ', (userToFollow) => {
            followUser(currentUser, userToFollow);
            mainLoop();
          });
        });
        break;
      case 'post':
        rl.question('Enter your username: ', (username) => {
          rl.question('Enter post content: ', (content) => {
            createPost(username, content);
            mainLoop();
          });
        });
        break;
      case 'like':
        rl.question('Enter your username: ', (username) => {
          rl.question('Enter post ID to like: ', (postId) => {
            likePost(username, parseInt(postId));
            mainLoop();
          });
        });
        break;
      case 'comment':
        rl.question('Enter your username: ', (username) => {
          rl.question('Enter post ID to comment on: ', (postId) => {
            rl.question('Enter comment content: ', (content) => {
              commentOnPost(username, parseInt(postId), content);
              mainLoop();
            });
          });
        });
        break;
      case 'display':
        rl.question('Enter post ID to display: ', (postId) => {
          displayPost(parseInt(postId));
          mainLoop();
        });
        break;
      case 'feed':
        rl.question('Enter your username: ', (username) => {
          displayFeed(username);
          mainLoop();
        });
        break;
      case 'exit':
        rl.close();
        break;
      default:
        console.log('Invalid command.');
        mainLoop();
    }
  });
}

console.log('Welcome to ArrayGram!');
mainLoop();