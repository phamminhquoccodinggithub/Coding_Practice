/* TODO: Practice C++ coding in https://developers.google.com/edu/c++/next-steps
Welcome to Artillery.
You are in the middle of a war and being charged by thousands of enemies.
You have one cannon, which you can shoot at any angle.
You only have 10 cannonballs for this target..
Let's begin...

The enemy is 507 feet away!!!
What angle? 25<
You over shot by 445
What angle? 15
You over shot by 114
What angle? 10
You under shot by 82
What angle? 12
You under shot by 2
What angle? 12.01
You hit him!!!
It took you 4 shots.
You have killed 1 enemy.
I see another one, are you ready? (Y/N) n

You killed 1 of the enemy.
*/

#include <iostream>
#include <math.h>
#include <string>

const float kVelocity = 200.0; // initial velocity of 200 ft/sec
const float kGravity = 32.2;   // gravity for distance calculation
const int kNumCannonBalls = 10;
const float kPi = 3.14;

void startUp();
int fire(int killed);

int main()
{
    startUp(); // This displays the introductory script.
    int killed = 0;
    char done;
    do
    {
        killed = fire(killed); // fire() contains the main loop of each round.
        std::cout << "I see another one, care to shoot again? (Y/N) " << std::endl;
        std::cin >> done;
    } while (done != 'n');
    std::cout << "You killed " << killed << " of the enemy." << std::endl;
    return 0;
}

void startUp()
{
    // This displays the introductory script.
    std::string script = "Welcome to Artillery.\
        You are in the middle of a war and being charged by thousands of enemies.\
        You have one cannon, which you can shoot at any angle.\
        You only have 10 cannonballs for this target..\
        Let's begin...";
    std::cout << script << std::endl;
}

int calDistance(float in_angle)
{
    // To calculate distance between player and enemy
    // in_angle is the angle the player has entered, converted to radians.
    float time_in_air = (2.0 * kVelocity * sin(in_angle)) / kGravity;
    return round((kVelocity * cos(in_angle)) * time_in_air);
}

int generateEnemy()
{
    // To generate enemy in random position
    int kDistanceMax = 1000, kDistanceMin = 100; // Initial const max and min distance to generate enemy
    // Seed the random number generator
    srand(time(0));
    int position = rand() % kDistanceMax + kDistanceMin;
    return position;
}

int fire(int killed)
{
    // Main loop for each round fire and return number of killed
    // param killed: number of initial killed
    bool knock = false;
    float in_angle;
    int num_remain_cannon_balls = kNumCannonBalls;
    int enemy_position = generateEnemy();
    std::cout << "The enemy is " << enemy_position << " feet away!!!" << std::endl;
    do
    {
        std::cout << "What angle?" << std::endl;
        std::cin >> in_angle;
        float angle = (in_angle * kPi) / 180.0;
        int distance = calDistance(angle) - enemy_position; // distance between ammo and enemy
        num_remain_cannon_balls--;
        if (distance <= 0)
        {
            knock = true;
            killed++;
            std::cout << "You hit him!!!" << std::endl;
            std::cout << "It took you " << kNumCannonBalls - num_remain_cannon_balls << " shots." << std::endl;
        }
        else
        {
            if (calDistance(angle) > enemy_position)
            {
                std::cout << "You over shot by " << distance << std::endl;
            }
            else
            {
                std::cout << "You under shot by " << abs(distance) << std::endl;
            }
        }
    } while (num_remain_cannon_balls > 0 && !knock);

    if (num_remain_cannon_balls <= 0)
        std::cout << "Out of ammo..." << std::endl;
    std::cout << "You have killed " << killed << " enemy." << std::endl;
    return killed;
}
