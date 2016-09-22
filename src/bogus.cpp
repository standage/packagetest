#include "bogus.hpp"

bogus::bogus() : data(0)
{

}

int bogus::get_double(int value)
{
    data = value * 2;
    return data;
}
