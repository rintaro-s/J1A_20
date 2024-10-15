#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char filename[256];
    char command[512];
    char output_name[256];

    // 読み込むCファイルの名前を入力
    printf("コンパイルするCファイルの名前を入力してください (拡張子なしでも可): ");
    scanf("%255s", filename);

    // 拡張子がない場合、.cを付ける
    if (strstr(filename, ".c") == NULL) {
        strcat(filename, ".c");
    }

    // 実行ファイル名を作成（拡張子を除去）
    strcpy(output_name, filename);
    output_name[strlen(output_name) - 2] = '\0'; // .cを取り除く

    // gccコマンドを作成
    snprintf(command, sizeof(command), "gcc %s -o %s", filename, output_name);

    // gccでコンパイル
    int compile_status = system(command);
    if (compile_status != 0) {
        printf("コンパイルに失敗しました。\n");
        return 1;
    }

    // コンパイルが成功した場合、実行ファイルを実行
    printf("コンパイルに成功しました。実行します...\n");
    system(output_name);

    return 0;
}
