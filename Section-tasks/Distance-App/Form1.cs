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
            Double speed = 0;
            speed = Double.Parse(Spdtxt.Text);
            Double Hours_trvld = 0;
            Hours_trvld = Double.Parse(Hrs_trvld.Text);
            Double distance = 0;
            distance = speed * Hours_trvld;
            resultlst.Text = distance.ToString();
            Double counter = 1;
            resultlst.Items.Clear();
            while (counter <= Hours_trvld)
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