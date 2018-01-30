BEGIN {
    width = 11;
}

$2 ~ /[0-9A-Z_]+_BASE/ {
    printf("# %s registers\n", substr($2, 0, length($2) - 5));
    printf("%-*s = %s\n", width, $2, $3);
}

$2 ~ /[0-9A-Z_]+/ && $3 ~ /HW_REGISTER_R[WO]/ {
    printf("%-*s = %s\n", width, $2, $4);
}
