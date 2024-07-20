from utils import handle_metadata

metadata_dict, code = handle_metadata("""//| stdin: 10
int n;
printf("Combien de lignes? ")
scanf("%d", &n);
printf("%d lignes", n);
""")

assert metadata_dict == {'stdin': '10'}

assert code == """int n;
printf("Combien de lignes? ")
scanf("%d", &n);
printf("%d lignes", n);
"""

print("Tests succeeded")