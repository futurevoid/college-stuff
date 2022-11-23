namespace Weight_App
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }


        private void masstxt_TextChanged(object sender, EventArgs e)
        {
            try 
            {
                int mass = int.Parse(masstxt.Text);
                double weight = mass * 9.81;
                weightval_lbl.Text = weight.ToString() + " N";
                switch (mass)
                {
                    case >1000:
                        weighthl.Text = "Too high";
                        break;

                    case < 10:
                        weighthl.Text = "Too Low";
                        break;

                    default:
                        break;




                }
            }
            catch (System.FormatException)
            {
                weightval_lbl.Text = "Invalid Value";
                weighthl.Text = "";
            }
            catch (System.OverflowException)
            {
                weightval_lbl.Text = "Too Large Value";
                weighthl.Text = "";
            }

        }
    }
}