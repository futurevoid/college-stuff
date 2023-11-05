namespace Distance_App
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Calcbtn_Click(object sender, EventArgs e)
        {
            try 
            {
                int speed = 0;
                speed = int.Parse(Spdtxt.Text);
                int Hours_trvld = 0;
                Hours_trvld = int.Parse(Hrs_trvld.Text);
                int distance = 0;
                distance = speed * Hours_trvld;
                resultlst.Text = distance.ToString();
                int counter = 1;
                resultlst.Items.Clear();
                while (counter <= Hours_trvld)
                {
                    distance = counter * speed;
                    resultlst.Items.Add($"after {Hours_trvld} hours passed , The distance is {distance.ToString()}");
                    counter++;
                }
            }
            
            catch (System.FormatException)
            {
                MessageBox.Show("Invalid Value");
               
            }
            catch (System.OverflowException)
            {
                MessageBox.Show("Too Large Value");
                
            }
        }
    }
}