/*
 *  UTF-8 character counter
 *  -----------------------
 *  Author: Vedarth K
 *
 *  UTF-8 character can be of maximum of 4 bytes
 *  UTF-8 character set includes ASCII, there is way to distinguish, MSB of
 *  ASCII character will always be 0 and that of UTF-8 characer will always
 *  be 1.
 *
 *  UTF-8 character can be decoded in following manner:
 *  First byte denotes how many bytes are to be read further to completely
 *  decode the character, which is enough to detect a UTF-8 character
 *  and skip appropriate number of bybtes.
 *
 *  Illustration:
 *  FIRST BYTE SEQUENCE | CHARACTER TYPE/NO. OF BYTES
 *  -------------------------------------------------
 *  0xxxxxxx            | ASCII/1
 *  11xxxxxx            | UTF-8/2
 *  111xxxxx            | UTF-8/3
 *  1111xxxx            | UTF-8/4
 *
 */

#include<stdio.h>

#define MAX_BYTES 4     // UTF-8 can have maximum of 4 bytes
#define MAX_LENGTH 200  // maximum number of characters
#define NEXT_LINE '\n'

// count UTF-8 characters from given sequence of characters
int count_utf8_chars(char const *, int);

// returns number of bytes for UTF-8 character (if one)
int utf8_char_bytes(char);

// get input string from STDIN
const char * get_input(char *);

int main(int argc, char *argv[])
{
    char str[MAX_LENGTH];

    while(get_input(str) != NULL)
    {
        fprintf(stdout, "%d\n", count_utf8_chars(str, MAX_LENGTH));
    }
    return 0;
}

int count_utf8_chars(char const *str, int length)
{
    int i = 0;
    int count = 0;
    int bytes_to_skip = 0;

    for(i = 0; str[i] != NEXT_LINE && i < length; i++)
    {
        bytes_to_skip = utf8_char_bytes(str[i]);

        // if there are UTF-8 character bytes we skip them
        if(bytes_to_skip > 0){
            i += bytes_to_skip;
            count++;
        }
    }

    return count;
}

int utf8_char_bytes(char ch)
{
    // first byte is 11xxxxxx
    unsigned short MASK_TWO_BYTES = 192;

    // first byte is 111xxxxx
    unsigned short MASK_THREE_BYTES = 224;

    // first byte is 1111xxxx
    unsigned short MASK_FOUR_BYTES = 240;

    if((ch & MASK_TWO_BYTES) == MASK_TWO_BYTES) return 1;
    if((ch & MASK_THREE_BYTES) == MASK_THREE_BYTES) return 2;
    if((ch & MASK_FOUR_BYTES) == MASK_FOUR_BYTES) return 3;

    return 0;
}

const char * get_input(char *str)
{
    return fgets(str, MAX_LENGTH, stdin);
}
