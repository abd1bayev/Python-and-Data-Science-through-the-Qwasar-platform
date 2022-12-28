char* rotone(char* param_1)
{
	char* reverseAlphabetsmall = "bcdefghijklmnopqrstuvwxyza";
  	char* reverseAlphabetbig = "BCDEFGHIJKLMNOPQRSTUVWXYZA";
    for (int i = 0; i < strlen(param_1); i++)
    {
      	if(param_1[i]>='a'&&param_1[i]<='z')
        {
        	param_1[i] = reverseAlphabetsmall[param_1[i]-'a'];
        }
 		else if (param_1[i]>='A'&&param_1[i]<='Z')
        {
        	param_1[i] = reverseAlphabetbig[param_1[i]-'A'];
        }
    }
    return param_1;
}