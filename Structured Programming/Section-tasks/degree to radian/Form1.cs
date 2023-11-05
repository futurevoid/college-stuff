namespace degree_to_radian
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            try
            {
                float degree = 0;
                degree = float.Parse(textBox1.Text);
                if (degree > 0)
                {
                    float radians = (float)((Math.PI / 180) * degree);
                    label1.Text = radians.ToString();
                }
            }
            catch (System.FormatException) 
            {
                label1.Text = "Invalid input";
            }
            catch(System.OverflowException) 
            {
                label1.Text = "number is overflowing";

            }

        }
    }
}