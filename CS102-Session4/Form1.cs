namespace CS102_Session4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            try
            {
                this.label2.Location = new System.Drawing.Point(379, 238);
                int num = int.Parse(textBox1.Text);

                // the number divided by to get the checker final value

                int i, checker = 0;

                for (i = 1; i <= num; i++)
                {
                    if (num % i == 0)
                    {
                        checker++;
                    }
                }

                if (checker == 2)
                {
                    label2.Location = new System.Drawing.Point(320, 237);
                    label2.Text = num + " is a prime number";
                }
                else
                {
                    label2.Location = new System.Drawing.Point(304, 235);
                    label2.Text = num + " is not a prime number";

                }
                
            }
            catch (System.FormatException)
            {
                label2.Text = "Result";
            }
        }
    }
}