import java.util.*;


public class gameBoard{
    ArrayList<ArrayList<String>> board = new ArrayList<ArrayList<String>>();
    int gameCounter;
    int turnCounter;
    String player = "X";
    String winner = null;
    int xWins = 0;
    int oWins = 0;


    public gameBoard(){
        ArrayList<String> rowList = new ArrayList<String>();
        rowList.add("-");
        rowList.add("-");
        rowList.add("-");
        for (int i = 0; i < 3; i++){
            board.add(rowList);
        }
        turnCounter = 0;
        this.showBoard();
    }

    public void showBoard() {
        System.out.println(player + "'s turn");
        System.out.println(board.get(0));
        System.out.println(board.get(1));
        System.out.println(board.get(2));
    }

    public void move(int row, int colm){
        board.get(row).set(colm, player);
        int c = 0;
        int r = 0;
        int d = 0;
        int rd = 0;
        for (int i = 0; i < 3; i++){
            if (board.get(row).get(i) == player){
                c++;
            }
            else if (board.get(i).get(colm) == player){
                r++;
            }
            else if (board.get(i).get(i) == player){
                d++;
            }
            else if (board.get(i).get(3-i+1) == player){
                rd++;
            }
        }
        if ((r == 3) | (c == 3) | (d == 3) | (rd == 3)){
            winner = player;
            System.out.println(player + " has won!");
            if (player == "X"){
                xWins++;
            }
            else{
                oWins++;
            }
            this.reset();
        }
        else{
            turnCounter++;
            if (player == "X"){
                player = "O";
            }
            else{
                player = "X";
            }
            this.showBoard();
        }
    }

    public void reset() {
        ArrayList<ArrayList<String>> newBoard = new ArrayList<ArrayList<String>>();
        ArrayList<String> rowList = new ArrayList<String>();
        rowList.add("-");
        rowList.add("-");
        rowList.add("-");
        newBoard.add(rowList);
        newBoard.add(rowList);
        newBoard.add(rowList);
        board = newBoard;
        turnCounter = 0;
        gameCounter++;
        if (player == "X"){
            player = "O";
        }
        else{
            player = "X";
        }
    }
    public static void main(String []args) {
        gameBoard myGame = new gameBoard();
        myGame.move(0,1);


    }
}