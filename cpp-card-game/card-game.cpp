#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <random>
#include <map>
using namespace std;

int random(int min, int max) //range : [min, max]
{
   static bool first = true;
   if (first) 
   {  
      srand( time(NULL) ); //seeding for the first time only!
      first = false;
   }
   return min + rand() % (( max + 1 ) - min);
}
string intToCard(int inte) {
  string end;
  if(inte == 1) {
    end = "Ace";
  } else if(inte == 11) {
    end = "Jack";
  } else if(inte == 12) {
    end = "Queen";
  } else if(inte == 13) {
    end = "King";
  } else {
    end = to_string(inte);
  }
  return end;
}
void clear() {
  cout << u8"\033[2J\033[1;1H";
}

class Card {
  public:
    int num;
    string suit;
};
void printDeck(vector<Card> deck) {
  cout << "ur deck:\n";
  for(int i = 0; i < 5; i++) {
    Card card = deck.at(i);
    cout << intToCard(card.num) << " of " << card.suit << endl;
  }
}
int calcDmg(Card playCard, Card enemCard) {
  if(playCard.suit != "Spades") { return 0; }
  int end = 0;
  end += playCard.num;
  if(enemCard.suit == "Clovers") {
    end -= enemCard.num;
  }
  return end;
}
int main() {
  string suits[4] = {"Spades", "Clovers", "Diamonds", "Hearts"};
  vector<Card> fulldeck;
  vector<Card> userdeck;
  vector<Card> enemdeck;
  vector<Card> discardpile;
  int ind = 0;
  for(int s = 0; s < 4; s++) {
    for(int n = 1; n <= 13; n++) {
      Card obj;
      obj.suit = suits[s];
      obj.num = n;
      fulldeck.push_back(obj);
    }
  }
  // auto rd = random_device {};
  // auto rng = default_random_engine {};
  shuffle(fulldeck.begin(), fulldeck.end(), random_device());
  for(int i = 0; i < 5; i++) {
    Card card = fulldeck.at(i);
    fulldeck.erase(fulldeck.begin()+i);
    userdeck.push_back(card);
  }
  for(int i = 0; i < 5; i++) {
    Card card = fulldeck.at(i);
    fulldeck.erase(fulldeck.begin()+i);
    enemdeck.push_back(card);
  }
  int health = 100;
  int enemhealth = 100;
  while (health > 0 && enemhealth > 0) {
    clear();
    printDeck(userdeck);
    cout << "Your health: " << health << "\n";
    cout << "Enemy health: " << enemhealth << "\n";
    cout << "[1]Attack\n[2]Pass\n:";
    int choix;
    cin >> choix;
    if(choix == 1) {
      clear();
      printDeck(userdeck);
      cout << "Your health: " << health << "\n";
      cout << "Enemy health: " << enemhealth << "\n";
      cout << "Select a card(1 for first, 2 for 2nd etc etc): ";
      int cardchoix;
      cin >> cardchoix;
      cardchoix -= 1;
      Card cardpicked = userdeck.at(cardchoix);
      cout << enemdeck.size();
      int x = random(0, 3);
      Card enemcard = enemdeck.at(x);
      cout << x;
      string inp;
      cin >> inp;
      if(cardpicked.suit == "Spades") {
        if(cardpicked.num > 1 || cardpicked.num < 11) {
          enemhealth -= calcDmg(cardpicked, enemcard);
        }
      } else if(cardpicked.suit == "Hearts") {
        health += cardpicked.num;
      }
      userdeck.erase(userdeck.begin()+cardchoix);
      if(enemcard.suit == "Spades") {
        if(enemcard.num > 1 || enemcard.num < 11) {
          health -= calcDmg(enemcard, cardpicked);
        }
      } else if(enemcard.suit == "Hearts") {
        enemhealth += enemcard.num;
      }
    }
  };
  return 0;
}
