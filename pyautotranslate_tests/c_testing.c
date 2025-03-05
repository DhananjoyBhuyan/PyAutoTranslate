# include <stdio.h>

int main() {
    // Define a 2D array of strings
    char A[3][10][10] = {
        {"item1", "item2"},
        {"item3", "item4"},
        {"item5", "item6"}
    };

    // Loop through the 2D array
    for (int i = 0; i < 3; i++) {
        printf("%s %s\n", A[i][0], A[i][1]); // Print the row
        for (int j = 0; j < 2; j++) {
            printf("%s\n", A[i][j]); // Print each item in the row
        }
    }

    return 0;
}
