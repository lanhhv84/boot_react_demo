import React, { Component } from 'react';
import './App.css';
import axios from 'axios';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {rest: "Not set"};
    axios.get('http://10.0.0.79:8080/index')
    .then(res => {
      this.setState({rest: res.data});
      console.log(res.data);
    })
    .catch(error => {})
    .then(() => {});
  }

  render() {
    
    
    return (
      <div className="App">
          <h1>{this.state.rest}</h1>
          <Game ></Game>
      </div>
    );
  }
}
class Square extends React.Component {
  render() {
    return (
      <button className="square" onClick={this.props.onClick}>
        {this.props.value}
      </button>
    );
  }
}

class Board extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      squares: Array(9).fill(null),
      isNext: true,
      status: 'Next player: X'
    };
  }

  handleClick(i) {
    const squares = this.state.squares.slice();
    var isNext = this.state.isNext;
    var winner = null;
    var status = 'Next player: ' + (!isNext ? 'X' : 'O')
    if (!squares[i]) {
      if (isNext === true) {
        
        squares[i] = 'X';
        if (this.calculateWinner(squares)) {
          winner = 'X'; 
          status = 'Winner player: X'; 
        }
      }
      else {
        squares[i] = 'O';
        if (this.calculateWinner(squares)) {
          winner = 'O';
          status = 'Winner player: O'; 
        }
      }
      isNext = !isNext;
      
      this.setState({squares: squares, isNext: isNext, status: status});
    }

    if (winner) {

    }
  }

  calculateWinner(squares) {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ];
    for (let i = 0; i < lines.length; i++) {
      const [a, b, c] = lines[i];
      if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
        return squares[a];
      }
    }
    return null;
  }

  renderSquare(i) {
    return (
      <Square
        value={this.state.squares[i]}
        onClick={() => this.handleClick(i)}
      />
    );
  }

  render() {
    

    return (
      <div>
        <div className="status">{this.state.status}</div>
        <div className="board-row">
          {this.renderSquare(0)}
          {this.renderSquare(1)}
          {this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}
          {this.renderSquare(4)}
          {this.renderSquare(5)}
        </div>
        <div className="board-row">
          {this.renderSquare(6)}
          {this.renderSquare(7)}
          {this.renderSquare(8)}
        </div>
      </div>
    );
  }
}

class Game extends React.Component {
  render() {
    return (
      <div className="game">
        <div className="game-board">
          <Board />
        </div>
        <div className="game-info">
          <div>{/* status */}</div>
          <ol>{/* TODO */}</ol>
        </div>
      </div>
    );
  }
}


export default App;
