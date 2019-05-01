import React, { Component } from "react";

class MyPosts extends Component {
    state = {};

  render() {
    return (
      <div>
        <h2>Private page test</h2>
        <p>You should be logged in to see this page.</p>
        <p>Do you wish to logout? If so, click here.</p>
      </div>
    );
  }
}

export default MyPosts;