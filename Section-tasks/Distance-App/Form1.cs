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
                Double speed = Double.Parse(spdtxt.Text);
                Double hrs_trvld = Double.Parse(hrtxt.Text);
                Double Distance = speed * hrs_trvld;
                MessageBox.Show($"Distance: {Distance}");
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