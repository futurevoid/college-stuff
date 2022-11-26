namespace Temperature_App
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Convbtn_Click(object sender, EventArgs e)
        {
            try
            {
                double C = 0;
                double F = 0;
                double counter = 0;
                Celsiuslst.Items.Clear();
                Fahrenheitlst.Items.Clear();
                while (counter <= 20)
                {
                    C = counter;
                    F = (C * 9) / 5 + 32;
                    Celsiuslst.Items.Add($"Celsius temperature : {C.ToString()}");
                    Fahrenheitlst.Items.Add($"Fahrenheit temperature = {F.ToString()}");
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