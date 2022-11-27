namespace Radian_to_degree
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
                float radian = 0;
                radian = float.Parse(textBox1.Text);
                if (radian > 0)
                {
                    float degree = (float)((180 / Math.PI) * radian);
                    label1.Text = degree.ToString();
                }
            }
            catch (System.FormatException)
            {
                label1.Text = "Invalid input";
            }
            catch (System.OverflowException)
            {
                label1.Text = "number is overflowing";

            }

        }
    }
}