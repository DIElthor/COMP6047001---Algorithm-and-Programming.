int main()
{
  int area,length,width,area2,length2,width2;
  length = 3;
  width = 5;
  area = length * width;
  printf ("First assignment : %d\n",area);
  printf ("Second assignment : \nAdd length ");
  scanf("%d",&length2);
  printf ("Add width ");
  scanf("%d",&width2);
  area2 = length2 * width2;
  printf ("%d",area2);
  return 0;
}
