using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
namespace CS102_Section2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }


         private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                Double grade = (Double)Convert.ToDouble(textBox1.Text);

                switch (grade)
                {
                    case >= 90:
                        MessageBox.Show("A");
                        this.Close();
                        break;

                    case >= 80:
                        MessageBox.Show("B");
                        this.Close();
                        break;

                    case >= 70:
                        MessageBox.Show("C");
                        this.Close();
                        break;

                    case >= 60:
                        MessageBox.Show("D");
                        this.Close();
                        break;

                    case < 60:
                        MessageBox.Show("F");
                        this.Close();
                        break;

                    default:
                        MessageBox.Show("Invalid Number");
                        this.Close();
                        break;



                }

            }
            catch (System.FormatException)
            {
                MessageBox.Show("Invalid datatype/format. only numbers");
                this.Close();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }

       
    }
}