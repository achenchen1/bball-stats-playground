#include <sqlite3.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    printf("%s\n", sqlite3_libversion());
    char test[] = "2021.db";
    char** errmsg = malloc(sizeof(char*));

    sqlite3 *db;
    int result = sqlite3_config(SQLITE_CONFIG_MULTITHREAD);
    printf("%d\n", result);
    result = sqlite3_open(test, &db);
    printf("%d\n", result);
    result = sqlite3_exec(db, "SELECT * FROM test_table", NULL, NULL, errmsg);
    printf("%d\n", result);

    return 0;
}
