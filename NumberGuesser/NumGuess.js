let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;
const generateTarget = () => {
   return Math.floor(Math.random()*10);
};
const getAbsoluteDistance = (a, b) => {
    return Math.abs(a-b);
};
const compareGuesses = (userGuess, computerGuess, secretTarget) => {
     if (userGuess < 0 || userGuess > 9) {
        window.alert('Your choice is out of range!');
     } else if ((getAbsoluteDistance(userGuess, secretTarget)) <= (getAbsoluteDistance(computerGuess, secretTarget))) {
        return true;
     } else if ((getAbsoluteDistance(computerGuess, secretTarget)) < (getAbsoluteDistance(userGuess, secretTarget))) {
        return false;
   } 
};
const updateScore = winner => {
    if (winner === 'human') {
        humanScore += 1;
    } else if (winner === 'computer') {
        computerScore += 1;
    }
};
const advanceRound = () => {
    currentRoundNumber += 1;
};